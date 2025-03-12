import globals from "globals";
import pluginJs from "@eslint/js";
import html from "eslint-plugin-html"


/** @type {import('eslint').Linter.Config[]} */
export default [
  {
    files: ["**/*.js"],
    languageOptions: {
      sourceType: "script",
      globals: globals.browser
    },
  },
  {languageOptions: { globals: globals.browser }},
  pluginJs.configs.recommended,
  {
    files: ["**/*.html"],
    plugins: { html },
    rules: {
      "no-unused-vars": "warn"
    }
  },
  {
    files: ["**/*.js"],
    // Уберите использование pluginJs.configs.recommended, чтобы не было конфликта
    // или добавьте сюда нужные правила, если необходимо
    rules: {
      "no-unused-vars": "warn",  // Отключаем для JS файлов
    }
  }

];