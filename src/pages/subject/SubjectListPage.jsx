import SubjectListPresenter from "./SubjectListPresenter";

import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

import { useNav } from "../../hooks/useNav";
import { getAllSubjects } from "../../services/subjectService";

const SubjectListPage = () => {
  const navigate = useNavigate();

  const [subjects, setSubjects] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // 탭바 내용 변경
  const { updateNavItems } = useNav();
  useEffect(() => {
    updateNavItems([
      { to: "/subjects/add", icon: "✚", text: "과목추가" },
      { icon: "≡", text: "전체 메뉴" },
    ]);

    return () => {
      updateNavItems([
        { to: "/subjects", icon: "✎", text: "시험보기" },
        { icon: "≡", text: "전체 메뉴" },
      ]);
    };
  }, [updateNavItems]);

  const handleSubjectClick = (subjectId) => {
    navigate(`/subjects/${subjectId}`);
  };

  const handleClickTitle = () => {
    navigate("/");
  };

  const handleSearchInputChange = (e) => {
    const searchKeyword = e.target.value;
    const filteredSubjects = subjects.filter((subject) =>
      subject.name.includes(searchKeyword)
    );
    setSubjects(filteredSubjects);
  };

  useEffect(() => {
    const fetchSubjects = async () => {
      setIsLoading(true);
      try {
        const response = await getAllSubjects();
        setSubjects(response);
      } catch (error) {
        setError(error);
      } finally {
        setIsLoading(false);
      }
    };
    fetchSubjects();
  }, []);

  return (
    <SubjectListPresenter
      handleSearchInputChange={handleSearchInputChange}
      handleClickTitle={handleClickTitle}
      handleClickSubject={handleSubjectClick}
      subjects={subjects}
      isLoading={isLoading}
      error={error}
    />
  );
};

export default SubjectListPage;
