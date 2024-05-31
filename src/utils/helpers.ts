export const getPyScriptUrl = (script: string): string => {
  return `${process.env.APP_BASE_URL}py/${script}`;
};
