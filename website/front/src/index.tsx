import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import HomePage from './pages/HomePage';
import LoginPage from './components/LoginPage';
import CandidateChoice from './components/CandidateChoice';
import VoteEndPage from './components/VoteEndPage';
import Accueil from './components/Accueil';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const router = createBrowserRouter([
  { 
    path: "/",
    element: <HomePage />,
    children: [
      {
        path: "",
        element: <Accueil />,
      },
      {
        path: "login" ,
        element: <LoginPage />
      },
      {
        path: "about",
        element: <div>About page</div>
      }
    ]
  },
  {
    path: "/admin",
    element: <HomePage />,
    children: [
      {
        path: "dashboard",
        element: <div>Dashboard</div>
      }
    ]
  },
  {
    path: "/votes",
    element: <HomePage />,
    children:[
      {
        path: "",
        element: <CandidateChoice />,
      },
      {
        path: "error",
        element: <VoteEndPage text="Vous ne pouvez pas voter avec ce compte !" />
      },
      {
        path: "done",
        element: <VoteEndPage text="Votre vote a été pris en compte !" />
      }
    ]
  }
]);

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
    <RouterProvider router={router} />
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

