// src/app/utils/cookie.util.ts
//placeholder function, needs to be tested

export function getCookie(name: string): string | null {
    const matches = document.cookie.match(new RegExp(
      `(?:^|; )${name.replace(/([.$?*|{}()[]\/+^])/g, '\\$1')}=([^;]*)`
    ));
    return matches ? decodeURIComponent(matches[1]) : null;
  }