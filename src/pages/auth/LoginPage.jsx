import { useState } from "react";
import { useNavigate } from "react-router-dom";
import LoginPresenter from "./LoginPresenter";

const LoginPage = () => {
  const navigate = useNavigate();
  const [values, setValues] = useState({
    email: "",
    password: "",
  });
  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues((prev) => ({
      ...prev,
      [name]: value,
    }));
    setErrors((prev) => ({
      ...prev,
      [name]: "",
    }));
  };

  const validateForm = () => {
    const newErrors = {};
    if (!values.email) {
      newErrors.email = "이메일을 입력해주세요";
    } else if (!/\S+@\S+\.\S+/.test(values.email)) {
      newErrors.email = "올바른 이메일 형식이 아닙니다";
    }
    if (!values.password) {
      newErrors.password = "비밀번호를 입력해주세요";
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    setIsLoading(true);
    try {
      // 임시 API 호출 로직
      await new Promise((resolve) => setTimeout(resolve, 1000));
      localStorage.setItem("token", "example_token"); // 실제 토큰으로 교체 예정
      navigate("/");
    } catch (error) {
      console.error(error);
      setErrors({
        submit: "로그인에 실패했습니다. 다시 시도해주세요.",
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <LoginPresenter
      values={values}
      errors={errors}
      isLoading={isLoading}
      handleChange={handleChange}
      handleSubmit={handleSubmit}
    />
  );
};

export default LoginPage;
