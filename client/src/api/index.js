import axios from 'axios';
import {toast} from 'react-toastify';
import {BASE_URL} from './constants';

const API = axios.create(
  { baseURL: `${BASE_URL}/api` },
  {
    headers: {
      'Content-Type': 'multipart/form-data'
  }}
);

API.interceptors.request.use((req) => {
  if (localStorage.getItem('profile')) {
    req.headers.Authorization = `Bearer ${JSON.parse(localStorage.getItem('auth')).access}`;
  } else {
    window.location.href = "/";
  }
  return req;
});

API.interceptors.response.use(
	(response) => response,
    async function errorfunc(error) {
		const originalRequest = error.config;

		if (typeof error.response === 'undefined') {
			toast.error('Server Error', {
            position: "top-right",
            autoClose: 5000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
        });
			return Promise.reject(error);
		}
    if(error.response.status === 401){
      localStorage.clear();
      window.location.href="/login";
    }


		// specific error handling done elsewhere
		return Promise.reject(error);
	}
);



export const getUserData = API.get('/user/data');
