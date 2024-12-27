import axios from "axios";
import { createContext, useState } from "react";

export const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [accessToken, setAccessToken] = useState(
    // 엑세스 토큰
    localStorage.getItem("accessToken")
  );
  const [refreshToken, setRefreshToken] = useState(
    // 리프레시 토큰
    localStorage.getItem("refreshToken")
  );

  // 인증된 axios 인스턴스 생성
  const authAxios = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
  });

  // 요청 인터셉터 - 모든 요청에 access 토큰 추가
  authAxios.interceptors.request.use(
    (config) => {
      if (accessToken) {
        config.headers["Authorization"] = `Bearer ${accessToken}`;
      }
      return config;
    },
    (error) => {
      Promise.reject(error); // 오류 반환
    }
  );

  // 응답 인터셉터 - access 토큰 만료시 재발급
  authAxios.interceptors.response.use(
    (response) => response,
    async (error) => {
      const originalRequest = error.config; // 오류가 발생한 요청

      // access 토큰 만료 && 재요청이 아닌 경우 && refresh 토큰이 있는 경우
      if (
        error.response.status === 401 &&
        !originalRequest._retry &&
        refreshToken
      ) {
        originalRequest._retry = true; // 재요청 플래그

        try {
          // 새로운 access 토큰 요청
          const res = await authAxios.post("/refresh", { refreshToken });
          const newAccessToken = res.data.accessToken;
          setAccessToken(newAccessToken);
          localStorage.setItem("accessToken", newAccessToken);

          // 새로운 access 토큰으로 재요청
          originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
          return authAxios(originalRequest);
        } catch (error) {
          // refresh 토큰 만료시 로그아웃
          console.error("Token refresh failed:", error);
          logout(); // 로그아웃
          return Promise.reject(error); // 오류 반환
        }
      }
      return Promise.reject(error);
    }
  );

  // login 함수
  const login = async (email, password) => {
    try {
      const res = await authAxios.post("/login", { email, password });

      const { access_token, refresh_token } = res.data;

      const accessToken = access_token;
      const refreshToken = refresh_token;

      setAccessToken(accessToken);
      setRefreshToken(refreshToken);

      localStorage.setItem("accessToken", accessToken);
      localStorage.setItem("refreshToken", refreshToken);

      return { success: true }; // 로그인 성공
    } catch (error) {
      console.error("Login failed:", error);
      return {
        success: false,
        error: error.response?.data?.message || "Login failed",
      }; // 로그인 실패
    }
  };

  // logout 함수
  const logout = () => {
    setAccessToken(null);
    setRefreshToken(null);

    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
  };

  return (
    <AuthContext.Provider
      value={{ authAxios, login, logout, isAuthenticated: !!accessToken }}
    >
      {children}
    </AuthContext.Provider>
  );
};
