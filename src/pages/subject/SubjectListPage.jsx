import SubjectListPresenter from "./SubjectListPresenter";

import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

import { getSubjects } from "../../utils/api";

const SubjectListPage = () => {
  const navigate = useNavigate();

  const [subjects, setSubjects] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

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
        const response = await getSubjects();
        setSubjects(response);
      } catch (error) {
        setError(error);
      } finally {
        setIsLoading(false);
      }
    };
    fetchSubjects();
  }, []);
  console.log(subjects);

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
