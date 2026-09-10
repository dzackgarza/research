// web-tree-sitter ships a UMD bundle with Node-only branches; the browser
// build must not try to resolve them.
module.exports = {
  resolve: {
    fallback: {
      "fs/promises": false,
      fs: false,
      path: false,
      module: false,
    },
  },
};
