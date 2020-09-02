APP_NAME?=$(shell pwd | xargs basename)

clean-up:
ifneq ($(shell docker ps --filter "name=${APP_NAME}" -aq 2> /dev/null | wc -l | bc), 0)
	@echo "\e[1m\033[33mRemoving containers\e[0m"
	@docker ps --filter "name=${APP_NAME}" -aq | xargs docker rm -f
endif

golang:
	@echo "\e[1m\033[33mDebug mode\e[0m"
	@$(eval APP_DIR:=/go/src/github.com/victorabarros/${APP_NAME})
	@docker run -it -v $(shell pwd):${APP_DIR} -w ${APP_DIR} \
		--name ${APP_NAME}-golang golang:1.14 bash
