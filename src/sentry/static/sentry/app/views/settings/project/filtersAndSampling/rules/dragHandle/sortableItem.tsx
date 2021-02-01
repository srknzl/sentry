import React from 'react';
import {useSortable} from '@dnd-kit/sortable';

import Item from './item';

type Props = Pick<React.ComponentProps<typeof Item>, 'renderItem'> & {
  id: string;
};

function SortableItem({id, renderItem}: Props) {
  const {
    attributes,

    listeners,
    setNodeRef,
    transform,
    transition,
  } = useSortable({id});

  return (
    <Item
      forwardRef={setNodeRef}
      value={id}
      transform={transform}
      transition={transition}
      listeners={listeners}
      renderItem={renderItem}
      {...attributes}
    />
  );
}

export default SortableItem;
