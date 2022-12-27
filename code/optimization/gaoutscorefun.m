function [state,options,optchanged] = gascoreoutfun(options,state,flag)
persistent history
optchanged = false;
switch flag
    case 'init'
        history = [min(state.Score),mean(state.Score)];
        assignin('base','gapopulationhistory',history);
    case 'iter'
        history = [history;min(state.Score),mean(state.Score)];
        assignin('base','gapopulationhistory',history);
    case 'done'
end
end