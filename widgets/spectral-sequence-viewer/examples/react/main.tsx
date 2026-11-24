import React from "react";
import { createRoot } from "react-dom/client";
import "../../dist/spectral-sequence-viewer.js";
import sequence from "../sequence.json";
createRoot(document.getElementById("root")!).render(
  <spectral-sequence-viewer
    ref={(el) => {
      if (el) el.sequence = sequence;
    }}
  />,
);
