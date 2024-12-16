export const createExamService = (authAxios) => ({
  getAllExams: async () => {
    const response = await authAxios.get("exams");
    return response.data;
  },

  createExam: async (data) => {
    const response = await authAxios.post("exams", data);
    return response.data;
  },

  getExam: async (examId) => {
    const response = await authAxios.get(`exams/${examId}`);
    return response.data;
  },

  updateExam: async (examId, data) => {
    const response = await authAxios.patch(`exams/${examId}`, data);
    return response.data;
  },

  deleteExam: async (examId) => {
    const response = await authAxios.delete(`exams/${examId}`);
    return response.data;
  },

  getQuestionsByExam: async (examId) => {
    const response = await authAxios.get(`exams/${examId}/questions`);
    return response.data;
  },
});
