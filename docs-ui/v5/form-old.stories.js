import React from 'react';
import {action} from '@storybook/addon-actions';
import {withInfo} from '@storybook/addon-info';
import PropTypes from 'prop-types';

import {Form as LegacyForm, TextField as LegacyTextField} from 'app/components/forms';

class UndoButton extends React.Component {
  handleClick(e) {
    e.preventDefault();
    this.context.form.undo();
  }

  render() {
    return (
      <button type="button" onClick={this.handleClick.bind(this)}>
        Undo
      </button>
    );
  }
}

UndoButton.contextTypes = {
  form: PropTypes.object,
};

export default {
  title: 'Core/Forms/Old/Form',
};

export const Empty = withInfo('Empty form')(() => (
  <LegacyForm onSubmit={action('submit')} />
));

Empty.storyName = 'empty';

export const WithCancel = withInfo(
  'Adds a "Cancel" button when `onCancel` is defined'
)(() => <LegacyForm onCancel={action('cancel')} onSubmit={action('submit')} />);

WithCancel.storyName = 'with Cancel';

export const SaveOnBlurAndUndo = withInfo('Saves on blur and has undo')(() => (
  <LegacyForm saveOnBlur allowUndo>
    <LegacyTextField
      name="name"
      label="Team Name"
      placeholder="e.g. Operations, Web, Desktop"
      required
    />
    <LegacyTextField name="slug" label="Short name" placeholder="e.g. api-team" />
    <UndoButton />
  </LegacyForm>
));

SaveOnBlurAndUndo.storyName = 'save on blur and undo';
