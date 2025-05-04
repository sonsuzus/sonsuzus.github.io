module.exports = {
  extends: ['@commitlint/config-conventional'],
  ignores: [
    (commit) =>
      commit.startsWith('Update') || // Genelde dependabot mesajları böyle başlar
      commit.includes('dependabot')  // dependabot tag'lı commit'leri de atla
  ],
};
