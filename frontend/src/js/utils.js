import moment from 'moment';

export default {
  getLogFileName() {
    return `log-${moment().format('YYYY-MM-DD')}.txt`;
  }
};
