import { Button } from "./components/ui/button";
import "./App.css";

const modules = [
  { label: "Registration", status: "Coming soon" },
  { label: "Duplicate review", status: "Coming soon" },
  { label: "Polling verification", status: "Coming soon" },
];

function App() {
  return (
    <main className="app-shell">
      <nav className="topbar" aria-label="Primary navigation">
        <a className="brand" href="/">
          <span className="brand-mark" aria-hidden="true">IV</span>
          <span>IrisVote</span>
        </a>
        <div className="nav-links">
          {modules.map((module) => (
            <a href={module.label === "Registration" ? "/register" : `#${module.label.toLowerCase().replaceAll(" ", "-")}`} key={module.label}>
              {module.label}
            </a>
          ))}
        </div>
      </nav>

      <section className="hero" aria-labelledby="hero-title">
        <div className="hero-copy">
          <p className="eyebrow">Biometric voter integrity platform</p>
          <h1 id="hero-title">A clearer view of voter identity.</h1>
          <p className="hero-description">
            IrisVote helps election teams identify potential duplicate registrations
            for careful, human-led investigation. This workspace is ready for the
            next stages of the prototype.
          </p>
          <div className="hero-actions">
            <a href="/register"><Button>Explore the workspace</Button></a>
            <a className="text-link" href="#how-it-works">How it works <span aria-hidden="true">→</span></a>
          </div>
        </div>
        <div className="iris-card" aria-label="IrisVote platform status">
          <div className="iris-glow" aria-hidden="true" />
          <div className="iris-card-content">
            <span className="status-dot" />
            <span>Prototype workspace</span>
            <strong>Built for responsible verification</strong>
            <p>Biometric signals create investigation alerts, never automatic rejection.</p>
          </div>
        </div>
      </section>

      <section className="module-section" id="how-it-works" aria-labelledby="modules-title">
        <div>
          <p className="eyebrow">A modular foundation</p>
          <h2 id="modules-title">Everything in one considered workflow.</h2>
        </div>
        <div className="module-grid">
          {modules.map((module, index) => (
            <article className="module-card" key={module.label}>
              <span className="module-number">0{index + 1}</span>
              <h3>{module.label}</h3>
              <p>{module.status}. This module will be introduced in a later stage.</p>
            </article>
          ))}
        </div>
      </section>

      <footer>
        <span>IrisVote</span>
        <span>Privacy-led by design · Stage 1 foundation</span>
      </footer>
    </main>
  );
}

export default App;
