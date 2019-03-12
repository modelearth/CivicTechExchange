// @flow

import SearchSortOptions from './Filters/SearchSortOptions.jsx';
import ResetSearchButton from './ResetSearchButton.jsx';
import AlertSignupModal from "./AlertSignupModal.jsx";
import metrics from "../../utils/metrics.js";
import React from 'react';

type State = {|
  showAlertSignupModal: boolean,
  searchFilters: ?string
|};

class ProjectSearchContainer extends React.PureComponent<{||}, State> {
  constructor(): void {
    super();
    this.state = {
      showAlertSignupModal: false,
      searchFilters: ""
    };
  }

  openAlertSignup() {
    this.setState({
      showAlertSignupModal: true,
      searchFilters: document.location.search
    });
    metrics.logUserAlertButtonClick();
  }

  handleCloseAlertSignup() {
    this.setState({showAlertSignupModal: false});
  }

  render(): React$Node {
    return (
      <div className="ProjectSearchContainer-root row">
        <div className="ProjectSearchContainer-reset col-12 col-md-3 col-xxl-2">
          <ResetSearchButton />
        </div>
        <div className="ProjectSearchContainer-search col-12 col-md-9 col-xxl-10">
          <SearchSortOptions />
        </div>
      </div>
    );
  }
}

export default ProjectSearchContainer;
