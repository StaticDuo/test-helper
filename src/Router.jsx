import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/auth/LoginPage";
import Layout from "./components/common/Layout";
import SubjectListPage from "./pages/subject/SubjectListPage";
import SubjectDetailPage from "./pages/subject/SubjectDetailPage";
import ExamUploadPage from "./pages/exam/ExamUploadPage";
import ExamTakingPage from "./pages/exam/ExamTakingPage";
import StatisticsPage from "./pages/statistics/StatisticsPage";
import PasswordResetPage from "./pages/auth/PasswordResetPage";
import SignupPage from "./pages/auth/SignupPage";

import ProtectedRoute from "./components/auth/ProtectedRoute";
import PublicRoute from "./components/auth/PublicRoute";

function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<PublicRoute />}>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/password-reset" element={<PasswordResetPage />} />
          <Route path="/signup" element={<SignupPage />} />
        </Route>
        <Route element={<ProtectedRoute />}>
          <Route path="/" element={<Layout />}>
            <Route index element={<SubjectListPage />} />
            <Route path="subjects/:subjectId" element={<SubjectDetailPage />} />
            <Route path="exams/upload" element={<ExamUploadPage />} />
            <Route path="exams/:examId/take" element={<ExamTakingPage />} />
            <Route path="statistics" element={<StatisticsPage />} />
          </Route>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default Router;
