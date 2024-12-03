import { useState } from "react";
import { useNavigate } from "react-router-dom";
import SignupPresenter from "./SignupPresenter";

import { userSignUp } from "../../services/authService";

const SignupPage = () => {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    email: "",
    password: "",
    passwordConfirm: "",
  });
  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);

  const validateForm = () => {
    const newErrors = {};

    // 이메일 검증
    if (!form.email) {
      newErrors.email = "이메일을 입력해주세요";
    } else if (!/\S+@\S+\.\S+/.test(form.email)) {
      newErrors.email = "올바른 이메일 형식이 아닙니다";
    }

    // 비밀번호 검증
    if (!form.password) {
      newErrors.password = "비밀번호를 입력해주세요";
    } else if (form.password.length < 8) {
      newErrors.password = "비밀번호는 8자 이상이어야 합니다";
    }

    // 비밀번호 확인 검증
    if (!form.passwordConfirm) {
      newErrors.passwordConfirm = "비밀번호 확인을 입력해주세요";
    } else if (form.password !== form.passwordConfirm) {
      newErrors.passwordConfirm = "비밀번호가 일치하지 않습니다";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const onChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({
      ...prev,
      [name]: value,
    }));
    // 해당 필드의 에러 메시지 초기화
    if (errors[name]) {
      setErrors((prev) => ({
        ...prev,
        [name]: "",
      }));
    }
  };

  const onSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    setIsLoading(true);
    try {
      // API 호출 로직
      const userInfo = await userSignUp({
        id: form.email,
        password: form.password,
      });
      console.log(userInfo);
      // 회원가입 성공 시 로그인 페이지로 이동
      navigate("/login");
    } catch (error) {
      console.error(error);
      setErrors((prev) => ({
        ...prev,
        submit: "회원가입에 실패했습니다. 다시 시도해주세요.",
      }));
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <SignupPresenter
      form={form}
      errors={errors}
      isLoading={isLoading}
      onChange={onChange}
      onSubmit={onSubmit}
    />
  );
};

export default SignupPage;
