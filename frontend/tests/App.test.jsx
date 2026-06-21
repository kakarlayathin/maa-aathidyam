import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import App from '../src/App';

describe('App Component', () => {
  it('renders without crashing', () => {
    render(<App />);
  });

  it('renders the sidebar with navigation items', () => {
    render(<App />);
    const sidebar = screen.getByRole('navigation');
    expect(sidebar).toBeInTheDocument();
    expect(screen.getAllByText(/Dashboard/i).length).toBeGreaterThan(0);
    expect(screen.getAllByText(/Users/i).length).toBeGreaterThan(0);
    expect(screen.getByText(/Analytics/i)).toBeInTheDocument();
    expect(screen.getByText(/Settings/i)).toBeInTheDocument();
  });

  it('renders the header with search bar', () => {
    render(<App />);
    expect(screen.getByPlaceholderText(/Search.../i)).toBeInTheDocument();
  });
});
