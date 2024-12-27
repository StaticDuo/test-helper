import { useEffect, useState } from "react";
import styled from "styled-components";
import { useAuth } from "../../hooks/useAuth";
import { createExamService } from "../../services/examService";

const EXAMS = [
  {
    id: 1,
    title: "2021년 1학기 중간고사",
    subject: "수학",
    date: "2021.05.15",
    score: 85,
    duration: "90분",
  },
  {
    id: 2,
    title: "2021년 1학기 기말고사",
    subject: "과학",
    date: "2021.06.20",
    score: 78,
    duration: "120분",
  },
  {
    id: 3,
    title: "2021년 1학기 기말고사",
    subject: "과학",
    date: "2021.06.20",
    score: 78,
    duration: "120분",
  },
  {
    id: 4,
    title: "2021년 1학기 기말고사",
    subject: "과학",
    date: "2021.06.20",
    score: 78,
    duration: "120분",
  },
  {
    id: 5,
    title: "2021년 1학기 기말고사",
    subject: "과학",
    date: "2021.06.20",
    score: 78,
    duration: "120분",
  },
  {
    id: 6,
    title: "2021년 1학기 기말고사",
    subject: "과학",
    date: "2021.06.20",
    score: 78,
    duration: "120분",
  },
  {
    id: 7,
    title: "2021년 1학기 기말고사",
    subject: "과학",
    date: "2021.06.20",
    score: 78,
    duration: "120분",
  },
  {
    id: 8,
    title: "2021년 1학기 기말고사",
    subject: "과학",
    date: "2021.06.20",
    score: 78,
    duration: "120분",
  },
  {
    id: 9,
    title: "2021년 1학기 기말고사",
    subject: "과학",
    date: "2021.06.20",
    score: 78,
    duration: "120분",
  },
];

const RecentExam = () => {
  const [exams, setExams] = useState([]);

  const { authAxios } = useAuth();
  const examService = createExamService(authAxios);

  useEffect(() => {
    setExams(EXAMS);
    const fetchExams = async () => {
      try {
        const res = await examService.getRecentExams(1);
        console.log(res);
      } catch (error) {
        console.error(error);
      }
    };
    fetchExams();
  }, []);

  return (
    <Container>
      <Title>최근 본 시험</Title>
      <ExamList>
        {exams.length === 0 ? (
          <EmptyMessage>최근 응시한 시험이 없습니다.</EmptyMessage>
        ) : (
          exams.map((exam) => (
            <ExamCard key={exam.id}>
              <ExamTitle>{exam.title}</ExamTitle>
              <ExamDetails>
                <ExamSubject>{exam.subject}</ExamSubject>
                <ExamInfo>
                  <div>{exam.date}</div>
                  <div>점수: {exam.score}</div>
                  <div>소요시간: {exam.duration}</div>
                </ExamInfo>
              </ExamDetails>
            </ExamCard>
          ))
        )}
      </ExamList>
    </Container>
  );
};

export default RecentExam;

const Container = styled.div`
  height: 100%;
  display: flex;
  flex-direction: column;
  padding-top: 24px;
  overflow: hidden; // 컨테이너 자체는 스크롤 방지
`;

const Title = styled.h2`
  flex-shrink: 0; // 타이틀 높이 고정
  font-size: 20px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 16px;
`;

const ExamList = styled.div`
  flex: 1;
  overflow-y: auto;
  min-height: 0;
  padding-right: 4px;
`;

const ExamCard = styled.div`
  background: white;
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
`;

const ExamTitle = styled.div`
  font-size: 16px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 8px;
`;

const ExamDetails = styled.div`
  display: flex;
  flex-direction: column;
  gap: 8px;
`;

const ExamSubject = styled.div`
  display: inline-block;
  background: #f3f4f6;
  color: #4b5563;
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
`;

const ExamInfo = styled.div`
  display: flex;
  gap: 12px;
  color: #6b7280;
  font-size: 14px;
`;

const EmptyMessage = styled.div`
  text-align: center;
  color: #6b7280;
  padding: 32px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
`;
