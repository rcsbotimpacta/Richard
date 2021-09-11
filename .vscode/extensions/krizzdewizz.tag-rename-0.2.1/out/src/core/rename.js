"use strict";
var parse = require('parse5');
function inRange(pos, start, len) {
    return start < pos && pos <= (start + len + 1);
}
;
// https://html.spec.whatwg.org/multipage/syntax.html#void-elements
var VOID_ELEMENTS = {};
['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr']
    .forEach(function (it) { return VOID_ELEMENTS[it] = true; });
function isVoidElement(name) {
    return VOID_ELEMENTS[name.toLowerCase()];
}
var START_LEN = 1; // <
var END_LEN = 2; // </
function findMatchingEnd(text, pos, hasVoidElements) {
    var starts = {};
    var depth = 0;
    var startFound;
    var startMatch;
    var endMatch;
    var toId = function (name) { return name + depth; };
    var isVoid = hasVoidElements ? isVoidElement : function () { return false; };
    var parser = new parse.SAXParser({ locationInfo: true });
    parser.on('startTag', function (name, attrs, selfClosing, location) {
        var voidd = selfClosing || isVoid(name);
        starts[toId(name)] = location;
        if (inRange(pos, location.startOffset, name.length)) {
            if (voidd) {
                startMatch = { length: name.length, start: location.startOffset + START_LEN };
                parser.stop();
            }
            else {
                startFound = { name: name, depth: depth, position: location.startOffset };
            }
        }
        if (!voidd) {
            depth++;
        }
    });
    parser.on('endTag', function (name, location) {
        depth--;
        if (startFound && startFound.name === name && startFound.depth === depth) {
            endMatch = { length: name.length, start: startFound.position + START_LEN, end: location.startOffset + END_LEN };
            parser.stop();
        }
        else if (inRange(pos, location.startOffset + 1, name.length)) {
            startMatch = { length: name.length, start: starts[toId(name)].startOffset + START_LEN, end: location.startOffset + END_LEN };
            parser.stop();
        }
    });
    parser.end(text);
    return endMatch || startMatch;
}
exports.findMatchingEnd = findMatchingEnd;
//# sourceMappingURL=rename.js.map