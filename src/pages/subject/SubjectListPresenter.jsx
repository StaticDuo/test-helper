import styled from "styled-components";

import SearchBox from "../../components/common/SearchBox";
import AllSubject from "../../components/subject/AllSubject";

const SubjectListPresenter = ({
  handleSearchInputChange,
  handleClickSubject,
  subjects,
}) => {
  return (
    <Container>
      <SearchBox onChange={handleSearchInputChange} />
      <AllSubject handleSubjectClick={handleClickSubject} subjects={subjects} />
    </Container>
  );
};

export default SubjectListPresenter;

const Container = styled.div`
  display: flex;
  flex-direction: column;
  background-color: #f9fafb;
  padding: 24px;
  height: 100%;
`;
