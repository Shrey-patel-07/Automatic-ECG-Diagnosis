import React from "react";

export const Loader = () => {
  return (
    <div>
      <div className="overlay show-overlay">
        <div className="loader-container">
          <div className="loader"></div>
          <div className="loader-text">Loading...</div>
        </div>
      </div>
    </div>
  );
};
