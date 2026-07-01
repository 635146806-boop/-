/* Frame Design System — 出海风险分析 */

:root {
  /* Background */
  --bg-primary:   #0A0A0F;
  --bg-grid:      #1A1A2E;
  --bg-gradient:  radial-gradient(circle at 50% 40%, #1a1a2e 0%, #0a0a0f 70%);

  /* Accent */
  --accent:       #00FF88;
  --accent-glow:  rgba(0, 255, 136, 0.3);
  --accent-warn:  #FF3366;
  --accent-warn-glow: rgba(255, 51, 102, 0.3);

  /* Text */
  --text-primary:   #FFFFFF;
  --text-secondary: #B0B0C0;
  --text-gold:      #FFD700;
  --text-muted:     #666666;

  /* Grid */
  --grid-color:     #1A1A2E;
  --grid-spacing:   60px;
  --grid-line:      1px;

  /* Spacing */
  --safe-top:     80px;
  --safe-bottom:  200px;  /* 底部 20% 预留主播位 */
  --safe-left:    80px;
  --safe-right:   80px;

  /* Typography Scale */
  --font-hero:      'Noto Sans SC', 'PingFang SC', sans-serif;
  --font-headline:  'Noto Sans SC', 'PingFang SC', sans-serif;
  --font-body:      'Noto Sans SC', 'PingFang SC', sans-serif;
  --font-data:      'DIN Alternate', 'Roboto Mono', monospace;

  --size-hero:      72px;
  --size-headline:  48px;
  --size-caption:   32px;
  --size-data:      96px;
  --size-label:     24px;

  /* Component */
  --radius-card:    16px;
  --radius-pill:    100px;
  --shadow-card:    0 8px 32px rgba(0, 0, 0, 0.5);
  --shadow-glow:    0 0 40px var(--accent-glow);
}

/* Base */
body {
  margin: 0;
  padding: 0;
  background: var(--bg-primary);
  font-family: var(--font-body);
  color: var(--text-primary);
  overflow: hidden;
}

/* Grid Background */
.grid-bg {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(var(--grid-color) var(--grid-line), transparent var(--grid-line)),
    linear-gradient(90deg, var(--grid-color) var(--grid-line), transparent var(--grid-line));
  background-size: var(--grid-spacing) var(--grid-spacing);
  opacity: 0.6;
  pointer-events: none;
}

/* Gradient Overlay */
.gradient-overlay {
  position: absolute;
  inset: 0;
  background: var(--bg-gradient);
  pointer-events: none;
}

/* Text Styles */
.text-hero {
  font-family: var(--font-hero);
  font-size: var(--size-hero);
  font-weight: 900;
  letter-spacing: -2px;
  line-height: 1.1;
  color: var(--text-primary);
}

.text-headline {
  font-family: var(--font-headline);
  font-size: var(--size-headline);
  font-weight: 700;
  line-height: 1.2;
  color: var(--text-primary);
}

.text-caption {
  font-family: var(--font-body);
  font-size: var(--size-caption);
  font-weight: 500;
  line-height: 1.4;
  color: var(--text-secondary);
}

.text-data {
  font-family: var(--font-data);
  font-size: var(--size-data);
  font-weight: 700;
  line-height: 1;
  color: var(--text-gold);
}

.text-label {
  font-family: var(--font-body);
  font-size: var(--size-label);
  font-weight: 400;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--text-muted);
}

/* Accent Glow */
.accent-glow {
  text-shadow: 0 0 20px var(--accent-glow), 0 0 40px var(--accent-glow);
}

.gold-glow {
  text-shadow: 0 0 20px rgba(255, 215, 0, 0.3), 0 0 40px rgba(255, 215, 0, 0.2);
}

.warn-glow {
  text-shadow: 0 0 20px var(--accent-warn-glow), 0 0 40px var(--accent-warn-glow);
}

/* Card Component */
.card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-card);
  padding: 24px;
  backdrop-filter: blur(10px);
}

.card-accent {
  border-color: var(--accent);
  background: rgba(0, 255, 136, 0.08);
  box-shadow: var(--shadow-glow);
}

.card-warn {
  border-color: var(--accent-warn);
  background: rgba(255, 51, 102, 0.08);
  box-shadow: 0 0 40px var(--accent-warn-glow);
}

/* Pill Tag */
.pill {
  display: inline-block;
  padding: 8px 20px;
  border-radius: var(--radius-pill);
  background: var(--accent);
  color: var(--bg-primary);
  font-size: var(--size-label);
  font-weight: 600;
}

.pill-warn {
  background: var(--accent-warn);
  color: var(--text-primary);
}

.pill-gold {
  background: var(--text-gold);
  color: var(--bg-primary);
}

/* Animation Utilities */
@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.05); opacity: 0.8; }
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.animate-pulse {
  animation: pulse 2s ease-in-out infinite;
}

.animate-float {
  animation: float 3s ease-in-out infinite;
}
