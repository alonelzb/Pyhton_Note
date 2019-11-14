```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date : 2019-11-14 10:33:12
__author__ = 'luozaibo'


import logging
logging.basicConfig(level=logging.INFO,
                    filename='output.log',
                    format='%(asctime)s - %(levelname)s -%(name)s - %(module)s - %(lineno)s : %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)

logger.debug("This is a debug log.")
logger.info("This is a info log.")
logger.warning("This is a warning log.")
logger.error("This is a error log.")
logger.critical("This is a critical log.")
```
