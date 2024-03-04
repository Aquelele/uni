% TSKS24 SB: Lab 2, part 4.1

% Adjust settings:
format long         % About 15 digits display precision
format compact      % Suppress blank lines

% Fresh start:
clear               % Clear workspace
close all           % Close all figures

% Parameters:
T=2.5;              % Duration
fs=4e4;             % Sampling frequency
N=T*fs;             % Number of sampels
n=0:N-1;            % Vector of sample indices
t=1/fs*n;           % Vector of sample instances
f1=8000;            % The frequency  of the signal
x1=sin(2*pi*f1*t);  % The signal as a vector of samples
