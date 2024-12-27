import styled from "styled-components";

import RecentExam from "../components/exam/RecentExam";
import SearchBox from "../components/common/SearchBox";

const HomePage = () => {
  return (
    <Container>
      <SearchBox />
      <RecentExam />
    </Container>
  );
};

export default HomePage;

const Container = styled.div`
  display: flex;
  flex-direction: column;
  background-color: #f8fafc;
  padding: 24px;
  height: 100%;
`;
