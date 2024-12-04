import styled from "styled-components";

const SubjectDetailPresenter = ({ exams, isLoading, error }) => {
  return (
    <>
      {exams.map((exam) => (
        <div key={exam.exam_id}>{exam.name}</div>
      ))}
    </>
  );
};

export default SubjectDetailPresenter;
