# fabula-db

Static frontend that provides a searchable reference of [Fabula Ultima](https://need.games/fabula-ultima/) classes, skills, spells as well as class-specific things
- This is written in Vue 3 with Vite, with the data stored in JSON files under [`./public/data`](./public/data).
- Refer to [this page](./docs/schema.md) for the expected JSON schema for the data.

## Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```
- This runs with base URL `/`, which is the expected default for local development.

### Compile and Minify for Production

```sh
npm run build
```
- This runs with base URL `/fabula-ultima/`, since this is expected to be run for Github Pages.

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```
