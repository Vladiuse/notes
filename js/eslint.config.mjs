import globals from "globals";
import pluginJs from "@eslint/js";
import html from "eslint-plugin-html"


/** @type {import('eslint').Linter.Config[]} */
export default [
  {files: ["**/*.js"], languageOptions: {sourceType: "script"}},
  {languageOptions: { globals: globals.browser }},
  pluginJs.configs.recommended,
  {
    files: ["**/*.html"],
    plugins: { html },
  },
];