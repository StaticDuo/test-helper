import ExamDetailPresenter from "./ExamDetailPresenter";

import { useNav } from "../../hooks/useNav";
import { useEffect, useState } from "react";
import { useLocation, useParams } from "react-router-dom";

import { getExam } from "../../services/examService";

const ExamDetailPage = () => {
  const {
    state: { subjectId },
  } = useLocation();
  const { examId } = useParams();

  const [exam, setExam] = useState([]);

  // 탭바 내용 변경
  const { updateNavItems } = useNav();
  useEffect(() => {
    const navItems = [
      { to: `/add/${subjectId}/exams`, icon: "✚", text: "시험추가" },
      { icon: "≡", text: "전체 메뉴" },
    ];

    const defaultItems = [
      { to: "/subjects", icon: "✎", text: "시험보기" },
      { icon: "≡", text: "전체 메뉴" },
    ];

    updateNavItems(navItems);
    return () => updateNavItems(defaultItems);
  }, [updateNavItems, subjectId]);

  // 시험 정보 가져오기
  useEffect(() => {
    const fetchExam = async () => {
      try {
        const res = await getExam(examId);
        setExam(res);
      } catch (error) {
        console.error(error);
      }
    };
    fetchExam();
  }, [examId]);

  const handleClickStartExam = () => {
    console.log("시험 시작");
  };

  return (
    <>
      <ExamDetailPresenter
        exam={exam}
        handleClickStartExam={handleClickStartExam}
      />
    </>
  );
};

export default ExamDetailPage;
