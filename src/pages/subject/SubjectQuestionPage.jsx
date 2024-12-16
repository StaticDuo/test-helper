import { useEffect, useState } from "react";
import SubjectQuestionPresenter from "./SubjectQuestionPresenter";
import { useNavigate, useParams } from "react-router-dom";
import { useNav } from "../../hooks/useNav";

const SubjectQuestionPage = () => {
  const { subjectId } = useParams();
  const navigate = useNavigate();

  const [isRandomOrder, setIsRandomOrder] = useState(true);
  const [questionCount, setQuestionCount] = useState("");
  const [error, setError] = useState("");

  // 탭바 내용 변경
  const { updateNavItems } = useNav();
  useEffect(() => {
    const navItems = [
      { icon: "<-", text: "이전 문제" },
      { icon: "≡", text: "전체 문제" },
      { icon: "->", text: "다음 문제" },
    ];

    const defaultItems = [
      { to: "/subjects", icon: "✎", text: "시험보기" },
      { icon: "≡", text: "전체 메뉴" },
    ];

    updateNavItems(navItems);
    return () => updateNavItems(defaultItems);
  }, [updateNavItems, subjectId]);

  const handleRandomOrderClick = () => {
    setIsRandomOrder((prev) => !prev);
  };

  const handleQuestionStartClick = () => {
    navigate(`/questions`);
    // `/subjects/${subjectId}/questions?limit=${limit}&randomOrder=${isRandomOrder}`
  };

  const handleLimitChange = (e) => {
    const value = e.target.value;
    setQuestionCount(value);

    if (value === "") {
      setError("");
    } else {
      const numValue = Number(value);
      if (numValue < 1) {
        setError("최소 1개 이상의 문제를 선택해주세요.");
      } else if (numValue > 100) {
        setError("최대 100개까지만 선택할 수 있습니다.");
      } else {
        setError("");
      }
    }
  };

  return (
    <SubjectQuestionPresenter
      handleRandomOrderClick={handleRandomOrderClick}
      handleQuestionClick={handleQuestionStartClick}
      handleLimitChange={handleLimitChange}
      questionCount={questionCount}
      error={error}
    />
  );
};

export default SubjectQuestionPage;
