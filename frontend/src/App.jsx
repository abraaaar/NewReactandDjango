import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import NormalUser from "./pages/NormalUser";
import Surgeon from "./pages/Surgeon";
import Teleradiologist from "./pages/Teleradiologist";
import Radiologist from "./pages/Radiologist";
import NotFound from "./pages/NotFound";
import ProtectedRoute from "./components/ProtectedRoute";

function Logout() {
    localStorage.clear();
    return <Navigate to="/login" />;
}

function RegisterAndLogout() {
    localStorage.clear();
    return <Register />;
}

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/logout" element={<Logout />} />
                <Route path="/register" element={<RegisterAndLogout />} />
                <Route path="/normaluser" element={<ProtectedRoute><NormalUser /></ProtectedRoute>} />
                <Route path="/surgeon" element={<ProtectedRoute><Surgeon /></ProtectedRoute>} />
                <Route path="/teleradiologist" element={<ProtectedRoute><Teleradiologist /></ProtectedRoute>} />
                <Route path="/radiologist" element={<ProtectedRoute><Radiologist /></ProtectedRoute>} />
                <Route path="" element={<NotFound />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
