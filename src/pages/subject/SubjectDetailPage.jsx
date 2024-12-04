import SubjectDetailPresenter from "./SubjectDetailPresenter";

import { getExamsBySubject } from "../../services/subjectService";

import { useEffect, useState } from "react";
const SubjectDetailPage = () => {
  const [exams, setExams] = useState([]);

  useEffect(() => {
    const fetchExams = async () => {
      try {
        const response = await getExamsBySubject(1);
        setExams(response);
      } catch (error) {
        console.error(error);
      }
    };
    fetchExams();
  }, []);

  return <SubjectDetailPresenter subjectId={1} exams={exams} />;
};

export default SubjectDetailPage;
