import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import HomePage from './pages/HomePage';
import LoginPage from './components/LoginPage';

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
        path: "" ,
        element: <LoginPage />
      },
    ]
  },
  {
    path: "/admin",
    element: <HomePage />,
    children: [
      // {
      //   path: "" ,
      //   element: <LoginPage />
      // },
      {
        path: "dashboard",
        element: <div>Dashboard</div>
      }
    ]
  },
  {
    path: "votes",
    element: <div>Page de connexion pour les votans</div>,
    children:[
      {
        path: "",
        element: <div>Vote</div>,
      },
      {
        path: "error",
        element: <div>Vous ne pouvez pas voter avec ce compte !</div>
      },
      {
        path: "finalize",
        element: <div>Faite le choix final</div>
      },
      {
        path: "done",
        element: <div>La confirmation du vote est partie</div>
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

