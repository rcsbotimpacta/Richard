/**
 * Rename HTML/XML tags.
 */
"use strict";
var vs = require('vscode');
var rename_1 = require('./core/rename');
var RENAME_PROVIDERS = ['html', 'xml', 'php'];
var RenameProvider = (function () {
    function RenameProvider() {
    }
    RenameProvider.prototype.provideRenameEdits = function (document, position, newName, token) {
        var found = rename_1.findMatchingEnd(document.getText(), document.offsetAt(position), document.languageId !== 'xml');
        if (!found) {
            return undefined;
        }
        var edit = new vs.WorkspaceEdit();
        var startPos = found.start;
        edit.replace(document.uri, new vs.Range(document.positionAt(startPos), document.positionAt(startPos + found.length)), newName);
        var endPos = found.end;
        if (typeof endPos === 'number') {
            edit.replace(document.uri, new vs.Range(document.positionAt(endPos), document.positionAt(endPos + found.length)), newName);
        }
        return edit;
    };
    return RenameProvider;
}());
function activate(context) {
    vs.languages.registerRenameProvider(RENAME_PROVIDERS, new RenameProvider());
}
exports.activate = activate;
//# sourceMappingURL=extension.js.map