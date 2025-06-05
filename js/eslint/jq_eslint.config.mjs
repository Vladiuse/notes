import globals from "globals";
import pluginJs from "@eslint/js";
import html from "eslint-plugin-html"


/** @type {import('eslint').Linter.Config[]} */
export default [
  {
    files: ["**/*.js"],
    languageOptions: {
      sourceType: "script",
      globals: {
        ...globals.browser,
         $: true,
        },
    },
  },
  {languageOptions: { globals: globals.browser }},
  pluginJs.configs.recommended,
  {
    files: ["**/*.html"],
    plugins: { html },
    rules: {
      "no-unused-vars": "warn"
    },
       languageOptions: {

      globals: {
        ...globals.browser, // Разворачиваем все глобальные переменные браузера
        $: true // Добавляем jQuery $ как глобальную переменную
      }
    },
  },
  {
    files: ["**/*.js"],
    rules: {
      "no-unused-vars": "warn",
    }
  }

];