import { useNavigate, useParams } from "react-router-dom";
import SubjectExamPresenter from "./SubjectExamPresenter";

import { getExamsBySubject, getSubject } from "../../services/subjectService";
import { useEffect, useState } from "react";
import { useNav } from "../../hooks/useNav";

const SubjectExamPage = () => {
  const [exams, setExams] = useState([]);
  const [subject, setSubject] = useState([]);

  const navigate = useNavigate();
  const { subjectId } = useParams();

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

  // 과목별 시험 정보 가져오기
  useEffect(() => {
    const fetchExams = async () => {
      try {
        const exams = await getExamsBySubject(subjectId);
        setExams(exams);
        const subject = await getSubject(subjectId);
        setSubject(subject);
      } catch (error) {
        console.error(error);
      }
    };
    fetchExams();
  }, [subjectId]);

  const handleClickExam = (examId) => {
    navigate(`/exams/${examId}`, { state: { subjectId: subjectId } });
  };

  return (
    <>
      <SubjectExamPresenter
        exams={exams}
        subject={subject}
        handleClickExam={handleClickExam}
      />
    </>
  );
};

export default SubjectExamPage;
