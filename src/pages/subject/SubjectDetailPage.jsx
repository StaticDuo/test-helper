import SubjectDetailPresenter from "./SubjectDetailPresenter";

import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";

import { useNav } from "../../hooks/useNav";
import { useEffect, useState } from "react";

import { getSubject } from "../../services/subjectService";

const SubjectDetailPage = () => {
  const [subject, setSubject] = useState([]);

  const { subjectId } = useParams();
  const navigate = useNavigate();

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

  // 과목 정보 가져오기
  useEffect(() => {
    const fetchSubject = async () => {
      try {
        const res = await getSubject(subjectId);
        setSubject(res);
      } catch (error) {
        console.error(error);
      }
    };
    fetchSubject();
  }, [subjectId]);

  const handleClickExam = () => {
    navigate(`/subjects/${subjectId}/exams`);
  };
  const handleClickQuestion = () => {
    navigate(`/subjects/${subjectId}/questions`);
  };

  return (
    <SubjectDetailPresenter
      handleClickExam={handleClickExam}
      handleClickQuestion={handleClickQuestion}
      subject={subject}
    />
  );
};

export default SubjectDetailPage;
