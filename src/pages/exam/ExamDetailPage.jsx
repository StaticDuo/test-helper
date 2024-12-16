import ExamDetailPresenter from "./ExamDetailPresenter";

import { useNav } from "../../hooks/useNav";
import { useEffect, useState } from "react";
import { useLocation, useParams } from "react-router-dom";

import { createExamService } from "../../services/examService";
import { useAuth } from "../../hooks/useAuth";

const ExamDetailPage = () => {
  const {
    state: { subjectId },
  } = useLocation();
  const { examId } = useParams();

  const [exam, setExam] = useState([]);

  const { authAxios } = useAuth();
  const examService = createExamService(authAxios);

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
        const res = await examService.getExam(examId);
        setExam(res);
      } catch (error) {
        console.error(error);
      }
    };
    fetchExam();
  }, [examId]);

  const handleClickStartExam = () => {
    alert("시험을 시작합니다.");
  };

  // useEffect(() => {
  //   const fetchExam = async () => {
  //     try {
  //       const res = await axiosInstance.get(`exams/${examId}/questions`);
  //       console.log(res.data);
  //     } catch (error) {
  //       console.error(error);
  //     }
  //   };
  //   fetchExam();
  // }, []);

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
