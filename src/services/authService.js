import { axiosInstance } from "../utils/api";

// 새로운 사용자 정보 생성
// Returns: UserResponse: 생성된 유저의 정보
export const userSignUp = async (data) => {
  const response = await axiosInstance.post("signup", data);
  return response.data;
};

// 사용자 로그인
// Returns: access token 정보
export const userLogin = async (data) => {
  const response = await axiosInstance.post("login", data);
  return response.data;
};

// 모든 사용자 정보
// Returns: List[UserResponse]: 사용자 정보 리스트
export const getAllUsers = async () => {
  const response = await axiosInstance.get("users");
  return response.data;
};

// 특정 아이디의 사용자 정보
// Returns: SubjectResponse: 조회된 사용자의 정보
export const getUser = async (userId) => {
  const response = await axiosInstance.get(`users/${userId}`);
  return response.data;
};

// 리프레시 토큰으로 엑세스 토큰 재발급
// Returns: access token 정보
export const getRefreshToken = async (token) => {
  const response = await axiosInstance.post("refresh", { token });
  return response.data;
};
