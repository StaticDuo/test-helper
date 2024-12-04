import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/common/Layout";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import PublicRoute from "./components/auth/PublicRoute";

// Auth pages
import LoginPage from "./pages/auth/LoginPage";
import SignupPage from "./pages/auth/SignupPage";
import PasswordResetPage from "./pages/auth/PasswordResetPage";

// Subject pages
import SubjectListPage from "./pages/subject/SubjectListPage";
import SubjectDetailPage from "./pages/subject/SubjectDetailPage";
import SubjectExamPage from "./pages/subject/SubjectExamPage";
import SubjectQuestionPage from "./pages/subject/SubjectQuestionPage";

// Exam pages
import ExamListPage from "./pages/exam/ExamListPage";
import ExamUploadPage from "./pages/exam/ExamUploadPage";
import ExamTakingPage from "./pages/exam/ExamTakingPage";
import ExamDetailPage from "./pages/exam/ExamDetailPage";

// Statistics pages
import StatisticsPage from "./pages/statistics/StatisticsPage";
import DetailedStatsPage from "./pages/statistics/DetailedStatsPage";

// Home page
import HomePage from "./pages/HomePage";

function Router() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Public Routes */}
        <Route element={<PublicRoute />}>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage />} />
          <Route path="/password-reset" element={<PasswordResetPage />} />
        </Route>

        {/* Protected Routes */}
        <Route element={<ProtectedRoute />}>
          <Route element={<Layout />}>
            {/* Home */}
            <Route index element={<HomePage />} />

            {/* Subjects */}
            <Route path="subjects">
              <Route index element={<SubjectListPage />} />
              <Route path=":subjectId">
                <Route index element={<SubjectDetailPage />} />
                <Route path="exams" element={<SubjectExamPage />} />
                <Route path="questions" element={<SubjectQuestionPage />} />
              </Route>
            </Route>

            {/* Exams */}
            <Route path="exams">
              <Route index element={<ExamListPage />} />
              <Route path="upload" element={<ExamUploadPage />} />
              <Route path=":examId">
                <Route index element={<ExamDetailPage />} />
                <Route path="take" element={<ExamTakingPage />} />
              </Route>
            </Route>

            {/* Statistics */}
            <Route path="statistics">
              <Route index element={<StatisticsPage />} />
              <Route path="detailed" element={<DetailedStatsPage />} />
            </Route>
          </Route>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default Router;
