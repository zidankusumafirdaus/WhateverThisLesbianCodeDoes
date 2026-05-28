import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:5000';

export const apiClient = axios.create({
    baseURL: API_BASE_URL,
});

export const buildIconUrl = (svgPath) => {
    if (!svgPath) {
        return null;
    }
    const normalizedPath = svgPath.startsWith('/') ? svgPath.slice(1) : svgPath;
    return `${API_BASE_URL}/api/icons/display/${normalizedPath}`;
};

export const getProjects = async (params = {}) => {
    const response = await apiClient.get('/api/projects/', {
        params: {
            page: 1,
            page_size: 12,
            ...params,
        },
    });
    return response.data?.data;
};