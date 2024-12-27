import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { useNav } from "../../hooks/useNav";
import { createSubjectService } from "../../services/subjectService";
import { useAuth } from "../../hooks/useAuth";

import SubjectQuestionPresenter from "./SubjectQuestionPresenter";

const SubjectQuestionPage = () => {
  const location = useLocation();
  const { subjectName, subjectId, limit, randomOrder } = location.state || {};

  console.log(subjectName);

  const { authAxios } = useAuth();
  const questionsService = createSubjectService(authAxios);

  // 상태 관리
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isLoading, setIsLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);

  // 문제 데이터 가져오기
  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        setIsLoading(true);
        // API 호출 - 실제 엔드포인트로 교체 필요
        const res = await questionsService.getQuestionsBySubject(
          subjectId,
          limit,
          randomOrder
        );
        // randomOrder가 true면 문제 순서를 섞음
        // if (randomOrder) {
        //   data = shuffleArray(data);
        // }

        setQuestions(res.data.content);
        console.log(res);
      } catch (error) {
        console.error("Error fetching questions:", error);
        // 에러 처리 로직 추가
      } finally {
        setIsLoading(false);
      }
    };

    fetchQuestions();
  }, [subjectId, limit, randomOrder]);

  // 탭바 내용 변경 및 네비게이션 핸들러
  const { updateNavItems } = useNav();
  useEffect(() => {
    const handlePrevQuestion = () => {
      if (currentIndex > 0) setCurrentIndex((prev) => prev - 1);
    };

    const handleNextQuestion = () => {
      if (currentIndex < questions.length - 1)
        setCurrentIndex((prev) => prev + 1);
    };

    const handleShowAllQuestions = () => {
      // 전체 문제 보기 모달 띄우기
      setIsModalOpen((prev) => !prev);
    };

    const navItems = [
      {
        icon: "<-",
        text: "이전 문제",
        action: handlePrevQuestion,
        disabled: currentIndex === 0,
      },
      { icon: "≡", text: "전체 문제", action: handleShowAllQuestions },
      {
        icon: "->",
        text: "다음 문제",
        action: handleNextQuestion,
        disabled: currentIndex === questions.length - 1,
      },
    ];

    const defaultItems = [
      { to: "/subjects", icon: "✎", text: "시험보기" },
      { icon: "≡", text: "전체 메뉴" },
    ];

    updateNavItems(navItems);
    return () => updateNavItems(defaultItems);
  }, [updateNavItems, subjectId, currentIndex, questions.length]);

  // 배열을 무작위로 섞는 함수
  // const shuffleArray = (array) => {
  //   const newArray = [...array];
  //   for (let i = newArray.length - 1; i > 0; i--) {
  //     const j = Math.floor(Math.random() * (i + 1));
  //     [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
  //   }
  //   return newArray;
  // };

  if (isLoading) {
    return (
      <div>
        <p>문제를 불러오는 중입니다...</p>
      </div>
    );
  }

  if (questions.length === 0) {
    return <div>문제를 불러오지 못했습니다.</div>;
  }

  const currentQuestion = questions[currentIndex];

  const handleSubmit = () => {
    // 시험 제출 처리 로직
    alert("시험을 제출합니다.");
  };

  return (
    <SubjectQuestionPresenter
      subjectName={subjectName}
      currentQuestion={currentQuestion}
      currentIndex={currentIndex}
      questions={questions}
      setCurrentIndex={setCurrentIndex}
      isModalOpen={isModalOpen}
      handleSubmit={handleSubmit}
    />
  );
};

export default SubjectQuestionPage;
