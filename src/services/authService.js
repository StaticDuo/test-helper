import { publicAxios } from "../utils/api";
// import { useAuth } from "../hooks/useAuth";

// 인증이 필요없는 api 호출들

// 새로운 사용자 정보 생성
// Returns: UserResponse: 생성된 유저의 정보
export const userSignUp = async (data) => {
  const response = await publicAxios.post("signup", data);
  return response.data;
};

// 사용자 로그인
// Returns: access token 정보
export const userLogin = async (data) => {
  const response = await publicAxios.post("login", data);
  return response.data;
};

// 리프레시 토큰으로 엑세스 토큰 재발급
// Returns: access token 정보
export const getRefreshToken = async (token) => {
  const response = await publicAxios.post("refresh", { token });
  return response.data;
};

// 인증이 필요한 api 들을 위한 함수 생성자

export const createAuthService = (authAxios) => ({
  // 모든 사용자 정보
  // Returns: List[UserResponse]: 사용자 정보 리스트
  getAllUsers: async () => {
    const res = await authAxios.get("users");
    return res.data;
  },

  // 특정 아이디의 사용자 정보
  // Returns: SubjectResponse: 조회된 사용자의 정보
  getUser: async (userId) => {
    const res = await authAxios.get(`users/${userId}`);
    return res.data;
  },
});
