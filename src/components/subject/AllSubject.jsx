import { useState, useEffect } from "react";
import styled from "styled-components";

const AllSubject = ({ handleSubjectClick, subjects }) => {
  const [subjectList, setSubjectList] = useState(subjects);

  useEffect(() => {
    setSubjectList(subjects);
  }, [subjects]);

  return (
    <Container>
      <Title>전체과목</Title>
      <SubjectList>
        {subjectList.length === 0 ? (
          <EmptyMessage>과목이 없습니다.</EmptyMessage>
        ) : (
          subjectList.map((subject) => (
            <SubjectCard
              key={subject.subject_id}
              onClick={() => handleSubjectClick(subject.subject_id)}
            >
              <SubjectName>{subject.name}</SubjectName>
              <SubjectInfo>{subject.description}</SubjectInfo>
            </SubjectCard>
          ))
        )}
      </SubjectList>
    </Container>
  );
};

export default AllSubject;

const Container = styled.div`
  display: flex;
  flex-direction: column;
  padding: 20px;
  background-color: #f9fafb;
  height: 100%;
  overflow: hidden;
`;

const Title = styled.h2`
  font-size: 20px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 16px;
  flex-shrink: 0; // 타이틀 높이 고정
`;

const SubjectList = styled.div`
  flex: 1;
  min-height: 0;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px;
  overflow-y: auto;
  padding: 4px;
`;

const SubjectCard = styled.div`
  background: white;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  cursor: pointer;
  transition: box-shadow 0.2s;

  &:hover {
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  }
`;

const SubjectName = styled.h3`
  font-size: 18px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 8px;
`;

const SubjectInfo = styled.p`
  font-size: 14px;
  color: #6b7280;
`;

const EmptyMessage = styled.p`
  font-size: 16px;
  color: #6b7280;
`;
