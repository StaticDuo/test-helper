export const createSubjectService = (authAxios) => ({
  getAllSubjects: async () => {
    const response = await authAxios.get("subjects");
    return response.data;
  },

  createSubject: async (data) => {
    const response = await authAxios.post("subjects", data);
    return response.data;
  },

  getSubject: async (subjectId) => {
    const response = await authAxios.get(`subjects/${subjectId}`);
    return response.data;
  },

  updateSubject: async (subjectId, data) => {
    const response = await authAxios.patch(`subjects/${subjectId}`, data);
    return response.data;
  },

  deleteSubject: async (subjectId) => {
    const response = await authAxios.delete(`subjects/${subjectId}`);
    return response.data;
  },

  getExamsBySubject: async (subjectId) => {
    const response = await authAxios.get(`subjects/${subjectId}/exams`);
    return response.data;
  },

  getQuestionsBySubject: async (subjectId, limit, randomize) => {
    const query = `?limit=${limit}&randomize=${randomize}`;
    const response = await authAxios.get(
      `subjects/${subjectId}/questions${query}`
    );
    return response.data;
  },
});
