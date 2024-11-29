import SubjectListPresenter from "./SubjectListPresenter";

import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

const SubjectListPage = () => {
  const navigate = useNavigate();

  const [subjects, setSubjects] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubjectClick = (subjectId) => {
    navigate(`/subjects/${subjectId}`);
  };

  useEffect(() => {}, []);

  return <SubjectListPresenter />;
};

export default SubjectListPage;
