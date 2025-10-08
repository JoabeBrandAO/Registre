import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import App from '../App';

describe('App Component', () => {
  it('renders welcome message', () => {
    render(<App />);
    const welcomeElement = screen.getByText(/registre/i);
    expect(welcomeElement).toBeInTheDocument();
  });

  it('displays navigation menu', () => {
    render(<App />);
    const navElement = screen.getByRole('navigation');
    expect(navElement).toBeInTheDocument();
  });
});
