// 로그인 폼 검증
export const validateEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

export const validatePassword = (password) => {
  if (password.length < 8) {
    return "비밀번호는 8자 이상이어야 합니다.";
  }
  if (!/[A-Z]/.test(password)) {
    return "대문자를 포함해야 합니다.";
  }
  if (!/[0-9]/.test(password)) {
    return "숫자를 포함해야 합니다.";
  }
  return null; // 유효한 경우
};
